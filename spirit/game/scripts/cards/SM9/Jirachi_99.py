from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    is_active_pokemon,
    stellar_wish,
)

card = PokemonCardDef(
    guid="54386056-c2f9-590a-ac80-c66c53060473",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Wish",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may look at the top 5 cards of your deck, reveal a Trainer card you find there, and put it into your hand. Then, shuffle the other cards back into your deck, and this Pok\u00e9mon is now Asleep.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=stellar_wish,
            activation=Activations.ONCE_PER_TURN,
            condition=is_active_pokemon,
        ),
        Attack(
            title="Slap",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)