from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_patch, syncroblast_damage


card = PokemonCardDef(
    guid="9ba1fa1f-1763-5b1d-9e6a-5e01ae420456",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Attack(
            title="Energy Patch",
            game_text="Take a basic Energy card attached to 1 of your Pok\u00e9mon and attach it to another of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_patch,
        ),
        Attack(
            title="Syncroblast",
            game_text="If Girafarig and the Defending Pok\u00e9mon don't have the same number of Energy cards attached to them, this attack's base damage is 10 instead of 40.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=syncroblast_damage(40, 10),
        ),
    ],
)
