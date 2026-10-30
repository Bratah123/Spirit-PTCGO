from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="2405559c-b1ea-50ba-9757-a39a085b1622",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksVulpix.Name",
    display_name="Brock's Vulpix",
    searchable_by=["Brock's Vulpix", "Basic", "BrocksVulpix"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Flame",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
