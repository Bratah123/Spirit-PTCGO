from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_vanish


card = PokemonCardDef(
    guid="b3bacf6f-20ab-5ae2-aedc-ed8abfac48d8",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown [V]",
    searchable_by=["Unown [V]", "Basic", "UnownV"],
    subtypes=["Basic"],
    collector_number=89,
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
            title="[Vanish]",
            game_text="When you play Unown [V] from your hand, you may flip a coin. If heads, return 1 of your Pok\u00e9mon with Unown in its name (other than Unown [V]) to your hand. (Discard all cards attached to that card.)",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            effect=unown_vanish,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
