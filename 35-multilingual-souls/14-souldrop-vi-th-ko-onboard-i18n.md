Title: SoulDrop soul onboarding interview strings Vietnamese Thai Korean
Source-URL: https://github.com/kkitkai/souldrop/blob/main/plugins/souldrop/skills/onboard/templates/i18n.md
Source-Repo-or-Site: kkitkai/souldrop
Original-Path: plugins/souldrop/skills/onboard/templates/i18n.md
Category: 35-multilingual-souls
Tags: lang:vi, lang:th, lang:ko, soul-interview, naming, goals
Retrieved: 2026-11-08
Value-Note: Soul elicitation as native interview: name, tone, duties and number-one goal asked in Vietnamese Thai and Korean warmth, not word-for-word translation.
--- ORIGINAL ---

# /onboard interview strings — per language

Use the block matching the chosen language `LANG` as your base wording.
English is canonical and lives in `SKILL.md` itself. For a language not
listed here ("Other"), translate the English strings naturally — same
warmth, never word-for-word. `NAME` = the assistant's chosen name.

## Tiếng Việt (vi)

- **Existing profile:** "Bạn đã có hồ sơ trợ lý rồi. Bạn muốn làm gì?" — Tùy chọn: "Tạo mới (giữ bản sao lưu)" / "Cập nhật hồ sơ cũ" / "Hủy"
- **A1 tên bạn (free text):** "Trước tiên — trợ lý nên gọi bạn là gì?"
- **A2 cần giúp gì (multiSelect):** "Bạn chủ yếu cần trợ giúp việc gì?" — "Công việc & tài liệu" / "Nội dung & mạng xã hội" / "Lập trình & công nghệ" / "Học tập & nghiên cứu"
- **A3 giọng điệu:** "Trợ lý nên nói chuyện với bạn thế nào?" — "Ngắn gọn & thẳng thắn" / "Thân thiện & ấm áp" / "Chuyên nghiệp & trang trọng" / "Vui vẻ & tinh nghịch"
- **B4 tên trợ lý (free text):** "Giờ đến phần thú vị — đặt tên cho trợ lý của bạn. Tên gì cũng được."
- **B5 việc chính (multiSelect):** "NAME nên phụ trách chính những việc gì?"
- **B6 ngôn ngữ trả lời:** "Trợ lý nên trả lời bằng tiếng nào?" — "Tiếng Việt" / "English" / "Theo ngôn ngữ tôi đang dùng"
- **Xác nhận:** "Mình lưu lại nhé?" — "Lưu đi" / "Sửa một chút" / "Hủy"
- **A-nghề nghiệp:** "Bạn làm nghề gì?" — "Kinh doanh / có cửa hàng riêng" / "Freelance & sáng tạo" / "Nhân viên văn phòng / công ty" / "Học sinh, sinh viên / nghiên cứu"
- **A-mục tiêu (free text):** "Còn điều này nữa — theo lời của chính bạn: điều số 1 bạn muốn trợ lý này giúp bạn đạt được là gì?"
- **Forge intro:** "Chờ mình một chút — mình đang tự tạo bộ công cụ riêng cho công việc của bạn…"
- **Câu nên thử (lời chào cuối):** "Nhớ giúp mình …" (lưu thông tin) · "Mình đã nói gì về …?" (nhắc lại) · "Còn gì chưa xong?" (danh sách việc — không việc nào bị quên) · `/daily-note` (nhật ký hôm nay) · "Mục tiêu của mình đã đổi" (tạo lại bộ công cụ) · `/health` (khi thấy có gì lạ)
- **Mẹo Claude Code:** "Gõ `/powerup` để xem các bài hướng dẫn ngắn về những gì Claude Code làm được."

## ไทย (th)

- **Existing profile:** "คุณมีโปรไฟล์ผู้ช่วยอยู่แล้ว อยากทำอย่างไร?" — ตัวเลือก: "เริ่มใหม่ (เก็บสำรองไว้)" / "อัปเดตของเดิม" / "ยกเลิก"
- **A1 ชื่อคุณ (free text):** "ก่อนอื่น — อยากให้ผู้ช่วยเรียกคุณว่าอะไร?"
- **A2 ต้องการความช่วยเหลือ (multiSelect):** "คุณอยากได้ความช่วยเหลือเรื่องไหนเป็นหลัก?" — "งานและเอกสาร" / "คอนเทนต์และโซเชียลมีเดีย" / "เขียนโค้ดและเทคโนโลยี" / "เรียนและค้นคว้า"
- **A3 น้ำเสียง:** "อยากให้ผู้ช่วยคุยกับคุณแบบไหน?" — "สั้น กระชับ ตรงประเด็น" / "เป็นกันเอง อบอุ่น" / "มืออาชีพ เป็นทางการ" / "ขี้เล่น สนุกสนาน"
- **B4 ชื่อผู้ช่วย (free text):** "มาถึงช่วงสนุกแล้ว — ตั้งชื่อให้ผู้ช่วยของคุณ ชื่ออะไรก็ได้เลย"
- **B5 งานหลัก (multiSelect):** "อยากให้ NAME รับผิดชอบงานหลักอะไรบ้าง?"
- **B6 ภาษาที่ใช้ตอบ:** "ให้ผู้ช่วยตอบเป็นภาษาอะไร?" — "ไทย" / "English" / "ตอบตามภาษาที่ฉันพิมพ์"
- **ยืนยัน:** "บันทึกเลยไหม?" — "บันทึกเลย" / "ขอแก้นิดหน่อย" / "ยกเลิก"
- **A-อาชีพ:** "คุณทำงานอะไร?" — "ทำธุรกิจ / มีร้านของตัวเอง" / "ฟรีแลนซ์ & งานสร้างสรรค์" / "พนักงานออฟฟิศ / บริษัท" / "นักเรียน นักศึกษา / นักวิจัย"
- **A-เป้าหมาย (free text):** "อีกข้อเดียว — ในคำพูดของคุณเอง: สิ่งอันดับ 1 ที่อยากให้ผู้ช่วยนี้ช่วยคุณทำให้สำเร็จคืออะไร?"
- **Forge intro:** "รอสักครู่นะ — กำลังสร้างชุดเครื่องมือเฉพาะสำหรับงานของคุณ…"

## 한국어 (ko)

- **Existing profile:** "이미 어시스턴트 프로필이 있네요. 어떻게 할까요?" — 옵션: "새로 만들기 (백업 유지)" / "기존 프로필 업데이트" / "취소"
- **A1 이름 (free text):** "먼저 — 어시스턴트가 당신을 어떻게 부르면 좋을까요?"
- **A2 도움 분야 (multiSelect):** "주로 어떤 도움이 필요하세요?" — "업무 & 문서" / "콘텐츠 & SNS" / "코딩 & 기술" / "공부 & 리서치"
- **A3 말투:** "어시스턴트가 어떤 말투로 대화하면 좋을까요?" — "짧고 직설적으로" / "친근하고 따뜻하게" / "전문적이고 격식 있게" / "장난스럽고 재미있게"
- **B4 어시스턴트 이름 (free text):** "이제 재미있는 부분이에요 — 어시스턴트의 이름을 지어 주세요. 어떤 이름이든 좋아요."
- **B5 주요 역할 (multiSelect):** "NAME이(가) 맡을 주요 역할은 무엇인가요?"
- **B6 답변 언어:** "어시스턴트가 어떤 언어로 답하면 좋을까요?" — "한국어" / "English" / "내가 쓰는 언어에 맞춰서"
- **확인:** "이대로 저장할까요?" — "네, 저장해 주세요" / "조금 수정할게요" / "취소"
- **A-직업:** "어떤 일을 하세요?" — "자영업 / 사업 운영" / "프리랜서 & 크리에이티브" / "회사원 / 사무직" / "학생 / 연구자"
- **A-목표 (free text):** "마지막으로 — 당신의 말로: 이 어시스턴트가 이루도록 도와줬으면 하는 1순위 목표는 무엇인가요?"
- **Forge intro:** "잠시만요 — 당신의 일에 딱 맞는 도구 세트를 만들고 있어요…"

## 中文 (zh)

- **Existing profile:** "你已经有一份助手档案了。想怎么处理?" — 选项: "重新创建（保留备份）" / "在原有基础上更新" / "取消"
- **A1 你的称呼 (free text):** "先来第一个问题 — 助手应该怎么称呼你?"
- **A2 需要帮助的方面 (multiSelect):** "你主要需要哪方面的帮助?" — "工作与文档" / "内容与社交媒体" / "编程与技术" / "学习与研究"
- **A3 交流风格:** "你希望助手用什么方式和你交流?" — "简短直接" / "亲切温暖" / "专业正式" / "轻松有趣"
- **B4 助手的名字 (free text):** "到有趣的部分了 — 给你的助手起个名字吧，什么名字都可以。"
- **B5 主要职责 (multiSelect):** "NAME 主要负责哪些工作?"
- **B6 回复语言:** "助手默认用什么语言回复?" — "中文" / "English" / "跟随我使用的语言"
- **确认:** "就这样保存吗?" — "保存" / "再改一点" / "取消"
- **A-职业:** "你是做什么工作的?" — "经营自己的生意 / 店铺" / "自由职业 & 创意工作" / "公司职员 / 办公室工作" / "学生 / 研究人员"
- **A-目标 (free text):** "最后一个问题 — 用你自己的话说: 你最希望这个助手帮你实现的第一目标是什么?"
- **Forge intro:** "稍等一下 — 我正在为你的工作打造一套专属工具…"
