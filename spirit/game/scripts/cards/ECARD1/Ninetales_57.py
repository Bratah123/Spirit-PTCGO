from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import ethereal_flame


card = PokemonCardDef(
    guid="a050a0a0-b781-5449-97b5-500576c8aa38",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Mislead",
            game_text="Flip 2 coins. If either of them is heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True, coins=2, min_heads=1),
        ),
        Attack(
            title="Ethereal Flame",
            game_text="Discard all Fire Energy cards attached to Ninetales. This attack does 30 damage plus 20 more damage for each card discarded this way.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=ethereal_flame,
        ),
    ],
)
