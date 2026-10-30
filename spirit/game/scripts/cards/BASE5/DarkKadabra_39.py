from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    all_conditions,
    no_special_conditions,
    no_wr_damage,
)
from spirit.game.card_effects.support_common import discard_then_draw, requires_hand


card = PokemonCardDef(
    guid="0fb62a92-5423-5a34-b3cb-6635d7a39b58",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkKadabra.Name",
    display_name="Dark Kadabra",
    searchable_by=["Dark Kadabra", "Stage 1", "DarkKadabra"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Matter Exchange",
            game_text="Once during your turn (before your attack), you may discard a card from your hand in order to draw a card. This power can't be used if Dark Kadabra is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=all_conditions(no_special_conditions, requires_hand(n=1)),
            effect=discard_then_draw(
                1, 1, optional=False, prompt="Choose a card to discard"),
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=no_wr_damage,
        ),
    ],
)
