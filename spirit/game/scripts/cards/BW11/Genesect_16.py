from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="374fa6ee-9290-59ba-80f8-85e09ced17cc",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic", "Genesect"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Gaia Blaster",
            game_text="Does 20 more damage for each Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.GRASS), 20, base=50),
        ),
    ],
)