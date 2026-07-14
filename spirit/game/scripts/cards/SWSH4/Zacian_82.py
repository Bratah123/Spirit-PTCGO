from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_pokemon_vmax

_opponent_has_vmax = lambda ctx: any(
    is_pokemon_vmax(p.archetype_id) for p in ctx.opponent_pokemon_in_play()
)

card = PokemonCardDef(
    guid="894c5061-8e44-5472-9611-2af49a1aaed7",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic", "Zacian"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=888,
    abilities=[
        Attack(
            title="Metal Armament",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Amazing Sword",
            game_text="If your opponent has any Pok\u00e9mon VMAX in play, this attack does 150 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=150,
            damage_operator="+",
            effect=bonus_if(_opponent_has_vmax, 150),
        ),
    ],
)