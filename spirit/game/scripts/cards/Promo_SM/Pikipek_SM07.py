from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="8739e6b5-f8e0-5ffb-a3fe-525a7af8d677",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    display_name="Pikipek",
    searchable_by=["Pikipek", "Basic", "Pikipek"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=731,
    abilities=[
        Attack(
            title="Nosedive",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=recoil_attack(20),
        ),
    ],
)