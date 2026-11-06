from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import jaw_clamp, screech


card = PokemonCardDef(
    guid="870ecf3e-8c1e-5d5e-9561-32d90ecd52dd",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw",
    searchable_by=["Croconaw", "Stage 1", "Croconaw"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Screech",
            game_text="Until the end of your next turn, if an attack damages the Defending Pok\u00e9mon (after applying Weakness and Resistance), that attack does 20 more damage to the Defending Pok\u00e9mon",
            cost={PokemonTypes.COLORLESS: 1},
            effect=screech(),
        ),
        Attack(
            title="Jaw Clamp",
            game_text="Until the end of your opponent's next turn, as long as Croconaw is your Active Pok\u00e9mon, the Defending Pok\u00e9mon can't retreat, and if the effect of an attack, Pok\u00e9mon Power, or Trainer card would change that player's Active Pok\u00e9mon, that part of the effect does nothing.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=jaw_clamp,
        ),
    ],
)
