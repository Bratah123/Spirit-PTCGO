from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="d9b575b0-d49c-523d-ba80-9a8db5cc01bc",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MKangaskhanEX.Name",
    display_name="M Kangaskhan-EX",
    searchable_by=["M Kangaskhan-EX", "MEGA", "EX", "MKangaskhanEX"],
    subtypes=["MEGA", "EX"],
    collector_number=79,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KangaskhanEX.Name",
    family_id=115,
    abilities=[
        Attack(
            title="Wham Bam Punch",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
    ],
)