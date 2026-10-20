from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_remaining


card = PokemonCardDef(
    guid="6656b0a6-5aff-5640-88f6-986f494b90ea",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2", "Jumpluff"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[
        Attack(
            title="Fluffy Transport",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Solar Step",
            game_text="This attack does 20 damage times the number of your remaining Prize cards.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_prizes_remaining('mine'), 20),
        ),
    ],
)