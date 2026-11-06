from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import strange_scent


card = PokemonCardDef(
    guid="9bbff0fe-fdcf-554b-aa8e-188d591b882c",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur", "Stage 1", "Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=2,
    abilities=[
        Attack(
            title="Strange Scent",
            game_text="Each player flips a coin. Each player who gets heads chooses a total of 3 damage counters from among his or her Pok\u00e9mon and removes them. (If the player's Pok\u00e9mon have fewer total damage counters than that, he or she removes all of them.)",
            cost={PokemonTypes.GRASS: 1},
            effect=strange_scent,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)
