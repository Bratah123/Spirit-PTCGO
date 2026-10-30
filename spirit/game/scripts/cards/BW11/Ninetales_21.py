from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.passives import effective_pokemon_types


def _color_match(ctx):
    """This Pokemon has a basic Energy attached of the Defending Pokemon's type."""
    d = ctx.defender
    if d is None:
        return False
    types = set(effective_pokemon_types(ctx.board, d))
    return any(is_basic_energy_card(e) and types & set(e.get_attribute(AttrID.POKEMON_TYPES) or [])
               for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="7a9d9259-6970-54b8-ad5e-8103d9c19421",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Color Coordination",
            game_text="If this Pok\u00e9mon has any basic Energy attached to it that is the same type as the Defending Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_color_match, 40),
        ),
    ],
)