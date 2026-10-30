from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import ink_spurt


card = PokemonCardDef(
    guid="40000f62-71d9-5a13-9b05-9e651d69c78b",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Constrict",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Octazooka",
            game_text="Flip a coin. If heads, whenever the Defending Pok\u00e9mon attacks, your opponent flips a coin. If tails, that attack does nothing. (Benching or evolving that Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.WATER: 3},
            damage=40,
            effect=ink_spurt,
        ),
    ],
)
