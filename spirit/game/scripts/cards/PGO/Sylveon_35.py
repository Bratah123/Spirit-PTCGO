from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import bonus_if, active_is


def _is_dragon(p):
    return PokemonTypes.DRAGON.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="952c22cb-ebfb-552c-b4e8-947c865d54e0",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1", "Sylveon"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Souvenir",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_hand(count=2),
        ),
        Attack(
            title="Wonder Flash",
            game_text="If your opponent's Active Pok\u00e9mon is a Dragon Pok\u00e9mon, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=bonus_if(active_is(_is_dragon), 90, base=90),
        ),
    ],
)