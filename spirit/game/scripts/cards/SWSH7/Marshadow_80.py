from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import Passive


def _is_rapid_strike_card(card):
    return is_pokemon_card(card) and "Rapid Strike" in subtypes_for(card.archetype_id)


class ShadowFlickerPassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is carrier:
            return count + 1
        return count


async def shadow_flicker(ctx):
    """10 damage. If the Defending Pokemon is Knocked Out during your next
    turn, take 1 more Prize card."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None:
        ctx.add_passive_through_own_next_turn(defender, ShadowFlickerPassive())


card = PokemonCardDef(
    guid="61197dd1-389f-59da-b240-7015c62b6188",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Rapid Strike", "Marshadow"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=80,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=802,
    abilities=[
        Attack(
            title="Rapid Hunt",
            game_text="Search your deck for up to 2 Rapid Strike cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                _is_rapid_strike_card, count=2, minimum=0,
                prompt="Choose up to 2 Rapid Strike cards to put into your hand.",
            ),
        ),
        Attack(
            title="Shadow Flicker",
            game_text="If the Defending Pok\u00e9mon is Knocked Out during your next turn, take 1 more Prize card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=shadow_flicker,
        ),
    ],
)