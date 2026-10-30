from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_tell


card = PokemonCardDef(
    guid="3cc5956a-f5bc-5721-804f-9a9d05aacc22",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownT.Name",
    display_name="Unown [T]",
    searchable_by=["Unown [T]", "Basic", "UnownT"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Tell]",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at your opponent's hand and show your hand to your opponent. This power can be used even if Unown [T] is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            effect=unown_tell,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
