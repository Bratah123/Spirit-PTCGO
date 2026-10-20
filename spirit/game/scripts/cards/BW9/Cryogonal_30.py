from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.attacks_common import lock_defender_attacks


def _is_water_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.WATER.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _cryofreeze(ctx):
    """Printed damage; discard an Energy from this Pokemon. The Defending
    Pokemon can't attack during your opponent's next turn."""
    await ctx.deal_damage()
    if ctx.attached_energies(ctx.attacker):
        await ctx.discard_energy_from(ctx.attacker, 1, minimum=1)
    lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="36a18b62-338a-5b75-9b8b-d75c6db60f44",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Team Plasma", "Cryogonal"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=30,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Call Sign",
            game_text="Search your deck for a Water Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_is_water_pokemon, count=1, minimum=0, reveal=True, prompt="Choose a Water Pokémon"),
        ),
        Attack(
            title="Cryofreeze",
            game_text="Discard an Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=_cryofreeze,
        ),
    ],
)