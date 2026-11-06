from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import discard_fire_or_nothing, screech


card = PokemonCardDef(
    guid="28dbbb4a-854e-5236-99fa-3ae579806e08",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Until the end of your next turn, if an attack damages the Defending Pok\u00e9mon (after applying Weakness and Resistance), that attack does 20 more damage to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=screech(),
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard 1 Fire Energy card attached to Houndoom or this attack does nothing.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=discard_fire_or_nothing,
        ),
    ],
)
