from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.passives import Passive


class ChromashiftPassive(Passive):
    """The holder's live types become its attached basic Energies' types."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        energy_types = []
        for child in carrier.children:
            if not is_basic_energy_card(child):
                continue
            for t in child.get_attribute(AttrID.POKEMON_TYPES) or []:
                if t not in energy_types:
                    energy_types.append(t)
        return energy_types or types

card = PokemonCardDef(
    guid="743c4a25-d2e0-553f-882b-a16401198f9b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Rapid Strike", "Kecleon"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=122,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Chromashift",
            game_text="This Pok\u00e9mon is the same type as any basic Energy attached to it. (If it has 2 or more different types of basic Energy attached, this Pok\u00e9mon is each of those types.)",
            passive=ChromashiftPassive(),
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)