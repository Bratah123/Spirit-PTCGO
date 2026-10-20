from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import stance_change, stance_change_condition
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="8c5a42ac-7213-53de-8260-5e0ba3bcacba",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=86,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Stance Change",
            game_text="Once during your turn (before your attack), you may switch this Pok\u00e9mon with an Aegislash in your hand. (Any cards attached to this Pok\u00e9mon, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.)",
            activation=Activations.ONCE_PER_TURN,
            condition=stance_change_condition,
            effect=stance_change,
        ),
        Attack(
            title="King's Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn. This Pok\u00e9mon can't use King's Shield during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=protect_next_turn(prevent=True),
            locks_next_turn=True,
        ),
    ],
)