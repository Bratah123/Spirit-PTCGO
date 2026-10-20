from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="35546c18-1feb-568e-8126-887f1f68b627",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name",
    display_name="Gorebyss",
    searchable_by=["Gorebyss", "Stage 1", "Gorebyss"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Captivate",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 10, base=30),
        ),
    ],
)