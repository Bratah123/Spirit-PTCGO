from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage
from spirit.game.card_effects.ecard import return_home


card = PokemonCardDef(
    guid="87c6a42b-928c-53d0-9c3f-64af003bf440",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightMachoke.Name",
    display_name="Light Machoke",
    searchable_by=["Light Machoke", "Stage 1", "LightMachoke"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Return Home",
            game_text="If you have any Benched Pok\u00e9mon, shuffle 1 of them and all cards attached to it into your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=return_home,
        ),
        Attack(
            title="Gentle Kick",
            game_text="If the Defending Pok\u00e9mon has no damage counters on it, this attack does 40 damage. If it has any, this attack does 20 damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            effect=bonus_if(has_damage("defender"), -20),
        ),
    ],
)
