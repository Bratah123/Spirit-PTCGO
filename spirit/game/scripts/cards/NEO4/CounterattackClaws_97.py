from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import counterattack_claws


card = PokemonToolCardDef(
    guid="7dd63a07-5714-5b3d-9cab-c7c9b3519ece",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterattackClaws.Name",
    display_name="Counterattack Claws",
    searchable_by=["Counterattack Claws", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Counterattack Claws",
            game_text="During your opponent's turn, if the Pokémon Counterattack Claws is attached to is your Active Pokémon and an opponent's attack damages it (even if it is Knocked Out), flip a coin. If heads, put 2 damage counters on the Defending Pokémon. Then, discard Counterattack Claws.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=counterattack_claws,
        ),
    ],
)
