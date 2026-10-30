from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="bc719633-18a0-5fad-834b-120fe4ff0558",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    display_name="Weepinbell",
    searchable_by=["Weepinbell", "Stage 1", "Weepinbell"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Corrosive Acid",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)