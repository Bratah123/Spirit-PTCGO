from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import selfdestruct_attack


card = PokemonCardDef(
    guid="e6c005f6-0c4e-5979-85b3-0c604512ca13",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=110,
    abilities=[
        Attack(
            title="Smog",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 10 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Weezing does 60 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=selfdestruct_attack(bench_damage=10, self_damage=60),
        ),
    ],
)
