from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for


def _night_marchers(ctx):
    """Pokemon in your discard pile that have the Night March attack."""
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c) and any(
        getattr(a, "title", None) == "Night March"
        for a in getattr(def_for(c.archetype_id), "abilities", []) or []))


card = PokemonCardDef(
    guid="1b4690fd-9d04-5d5e-84ba-df70f63533c3",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic", "Pumpkaboo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=710,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Night March",
            game_text="This attack does 20 damage times the number of Pok\u00e9mon in your discard pile that have the Night March attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(_night_marchers, 20),
        ),
    ],
)