from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


def _named(p, *names):
    return getattr(def_for(p.archetype_id), "display_name", None) in names


def _partner_benched(ctx):
    return any(_named(p, 'Latias') for p in ctx.my_bench())


card = PokemonCardDef(
    guid="bb5efee1-27c7-54c8-b394-2aaa4480d5d4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Sky Blade",
            game_text="If Latias is on your Bench, this attack does 50 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_partner_benched, 50),
        ),
    ],
)