from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="915e07ed-86b4-5077-bb2f-9088aa1fc2df",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora", "Basic", "Zeraora"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=807,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Wild Charge",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(20),
        ),
    ],
)