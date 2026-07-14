from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="336fea38-bce6-5ec2-ad53-2370a7663fe2",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitan.Name",
    display_name="Galarian Darmanitan",
    searchable_by=["Galarian Darmanitan", "Stage 1", "GalarianDarmanitan"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=spread_damage(10, also_base=True),
        ),
        Attack(
            title="Crushing Headbutt",
            game_text="During your next turn, this Pok\u00e9mon can't use Crushing Headbutt.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            locks_next_turn=True,
        ),
    ],
)