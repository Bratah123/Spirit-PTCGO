from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.passives_common import is_in_active_spot


def _dynamotor_condition(board, player_id, pokemon):
    bench = board.find_player_area(player_id, "bench")
    if not bench or not bench.children:
        return False
    discard = board.find_player_area(player_id, "discard")
    cards = discard.children if discard else []
    return any(is_lightning_energy(c) for c in cards)


card = PokemonCardDef(
    guid="02d6b223-273b-548e-bdd0-e67ba16dadf6",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1", "Flaaffy"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Dynamotor",
            game_text="Once during your turn (before your attack), you may attach a Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_dynamotor_condition,
            effect=attach_from_discard(
                predicate=is_lightning_energy, count=1, minimum=0,
                target=lambda p: not is_in_active_spot(p),
                prompt="Choose a Lightning Energy card to attach to a Benched Pok\u00e9mon",
            ),
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)