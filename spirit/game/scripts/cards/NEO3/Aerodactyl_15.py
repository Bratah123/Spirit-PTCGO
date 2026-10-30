from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import prehistoric_memory
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="38ab3880-6b7d-534e-ab01-313aeb8e2a94",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Prehistoric Memory",
            game_text="Whenever an Evolved Pok\u00e9mon attacks (even if it's your opponent's), it can use any attack from its Basic Pok\u00e9mon card or any Evolution card attached to it. It still has to pay for that attack's Energy cost. This power stops working while Aerodactyl is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=prehistoric_memory,
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Aerodactyl. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=flip_or_nothing(then=protect_next_turn(prevent=True, effects_too=True)),
        ),
    ],
)
