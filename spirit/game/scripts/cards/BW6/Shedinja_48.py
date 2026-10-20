from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.session.passives import Passive


class _EmptyShellPassive(Passive):
    """If this Pokemon is Knocked Out, the opponent takes no Prize cards for it."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        return 0 if pokemon is carrier else count


card = PokemonCardDef(
    guid="da216ba6-34ab-58c4-b490-858c74ba2605",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Empty Shell",
            game_text="If this Pok\u00e9mon is Knocked Out, your opponent can't take any Prize cards for it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_EmptyShellPassive(),
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(3, 'choose_any_opponent'),
        ),
    ],
)