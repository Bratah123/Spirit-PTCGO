from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="00fe26b0-03f9-5898-b0e5-34d69140da53",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name",
    display_name="Dragapult",
    searchable_by=["Dragapult", "Stage 2", "Dragapult"],
    subtypes=["Stage 2"],
    collector_number=89,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Dragon Launcher",
            game_text="Discard a number of your Benched Dreepy up to the number of your opponent's Pok\u00e9mon in play. Then, for each Dreepy you discarded in this way, choose 1 of your opponent's Pok\u00e9mon and do 100 damage to it. You can't choose the same Pok\u00e9mon more than once. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)