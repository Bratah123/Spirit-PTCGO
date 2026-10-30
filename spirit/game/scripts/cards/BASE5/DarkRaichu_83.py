from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import surprise_thunder


card = PokemonCardDef(
    guid="c013607b-3719-5aee-b429-7d721878bed0",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkRaichu.Name",
    display_name="Dark Raichu",
    searchable_by=["Dark Raichu", "Stage 1", "DarkRaichu"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="BASE5",
    rarity=Rarities.RareSecret,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=26,
    abilities=[
        Attack(
            title="Surprise Thunder",
            game_text="Flip a coin. If heads, flip another coin. If the second coin is heads, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. If the second coin is tails, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            effect=surprise_thunder,
        ),
    ],
)
