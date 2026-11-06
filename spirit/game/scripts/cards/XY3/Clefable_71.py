from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.passives_common import debuff_defender_attacks


card = PokemonCardDef(
    guid="41fb256b-742d-5315-ad8a-66caeaa7e5c6",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Follow Me",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 30 (before applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=debuff_defender_attacks(30),
        ),
    ],
)