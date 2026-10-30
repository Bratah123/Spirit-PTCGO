from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    cunning, cunning_condition, no_weakness_or_resistance,
)


card = PokemonCardDef(
    guid="4eccbf9b-71fb-568c-85d8-d2bb0cdd9f52",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSlowking.Name",
    display_name="Dark Slowking",
    searchable_by=["Dark Slowking", "Stage 1", "DarkSlowking"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=199,
    abilities=[
        Ability(
            title="Cunning",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at the top card of your opponent's deck. Then, you may have your opponent shuffle his or her deck. This power can't be used if Dark Slowking is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=cunning_condition,
            effect=cunning,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness or Resistance for this attack.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=no_weakness_or_resistance,
        ),
    ],
)
