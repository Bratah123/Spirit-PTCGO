from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card


def _is_fighting_energy(card):
    return energy_provides_type(card, PokemonTypes.FIGHTING.value)


_has_fighting_energy_in_discard = requires_discard(_is_fighting_energy)


def mystery_charge_condition(board, player_id, pokemon):
    area = board.find_player_area(player_id, "discard")
    discard = list(area.children) if area else []
    if any(is_supporter_card(c) for c in discard):
        return False
    return _has_fighting_energy_in_discard(board, player_id, pokemon)


mystery_charge = attach_from_discard(
    predicate=_is_fighting_energy, count=1, target="choice",
    prompt="Choose a Fighting Energy card to attach.",
)

card = PokemonCardDef(
    guid="9fffbd7c-da97-5852-bc46-548959b8a728",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Mystery Charge",
            game_text="You can use this Ability only if you have no Supporter cards in your discard pile. Once during your turn, you may attach a Fighting Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=mystery_charge_condition,
            effect=mystery_charge,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)