from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import attach_from_discard


def _dynamotor_condition(board, player_id, pokemon):
    bench = board.find_player_area(player_id, "bench")
    if not bench or not bench.children:
        return False
    discard = board.find_player_area(player_id, "discard")
    cards = discard.children if discard else []
    return any(is_lightning_energy(c) for c in cards)


card = PokemonCardDef(
    guid="cc4ec52a-8c39-5a65-8684-e3eb4fdbd7d1",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=602,
    abilities=[
        Ability(
            title="Dynamotor",
            game_text="Once during your turn (before your attack), you may attach a Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_dynamotor_condition,
            effect=attach_from_discard(
                predicate=is_lightning_energy, count=1, minimum=0,
                target=lambda p: not is_in_active_spot(p),
                prompt="Choose a Lightning Energy card to attach to a Benched Pokémon",
            ),
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
