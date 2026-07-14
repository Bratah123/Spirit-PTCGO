from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard, recoil_attack
from spirit.game.session.effects import is_pokemon_card


def _is_fighting_pokemon(card):
    return is_pokemon_card(card) and \
        PokemonTypes.FIGHTING.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="7313c25e-63b7-52bf-82c1-69dd4e02e6d5",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Macho Revenge",
            game_text="This attack does 20 damage for each Fighting Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_discard("mine", pred=_is_fighting_pokemon), 20),
        ),
        Attack(
            title="Dynamite Punch",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=recoil_attack(50),
        ),
    ],
)