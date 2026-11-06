from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mirror_move, mirror_move_condition


card = PokemonCardDef(
    guid="e6f1a949-8858-52df-a5ac-5069b7f2b266",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    display_name="Spearow",
    searchable_by=["Spearow", "Basic", "Spearow"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=21,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Mirror Move",
            game_text="If Spearow was attacked last turn, do the final result of that attack on Spearow to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            condition=mirror_move_condition,
            effect=mirror_move,
        ),
    ],
)
