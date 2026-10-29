from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.support_common import search_attach_energy


def _is_fire_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIRE.value in types


async def blizzard_loop(ctx):
    """160 damage, then put all Energy attached to this Pokemon into your
    hand."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        await ctx.put_in_hand(energies, reveal=False)


card = PokemonCardDef(
    guid="6f6cb748-ecb2-59ba-8969-8e71c94df424",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=111,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=search_attach_energy(predicate=_is_fire_energy, count=1, to_self=True),
        ),
        Attack(
            title="Loop-the-Loop",
            game_text="Put all Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=blizzard_loop,
        ),
    ],
)