from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


card = PokemonCardDef(
    guid="e1d2f9d6-eb05-5c24-bf4b-6ae18522c02d",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Unyielding Rock",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: _is_pokemon_ex(ctx.defender), 60),
        ),
    ],
)