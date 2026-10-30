from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_laugh


card = PokemonCardDef(
    guid="35af0226-4a8d-57b3-8578-0a3565f5c4a7",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownL.Name",
    display_name="Unown [L]",
    searchable_by=["Unown [L]", "Basic", "UnownL"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Laugh]",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, each player shuffles his or her deck. This power can be used even if Unown [L] is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            effect=unown_laugh,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
