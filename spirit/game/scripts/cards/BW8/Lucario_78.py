from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_metal_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


class _DualArmorPassive(Passive):
    """If this Pokemon has any Metal Energy attached, its type is both Fighting and Metal."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return types
        if any(_is_metal_energy(c) for c in pokemon.children) \
                and PokemonTypes.METAL.value not in types:
            return list(types) + [PokemonTypes.METAL.value]
        return types


card = PokemonCardDef(
    guid="0c4c6021-054d-5264-8202-8d4cb6872604",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="If this Pok\u00e9mon has any Metal Energy attached to it, this Pok\u00e9mon's type is both Fighting and Metal.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_DualArmorPassive(),
        ),
        Attack(
            title="Hurricane Kick",
            game_text="Does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_prizes_taken('opponent'), 30, base=60),
        ),
    ],
)