from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import bench_guard_passive


card = PokemonCardDef(
    guid="4daeebfe-1597-526b-a811-369798f83585",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksRhydon.Name",
    display_name="Brock's Rhydon",
    searchable_by=["Brock's Rhydon", "Stage 1", "BrocksRhydon"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksRhyhorn.Name",
    family_id=111,
    abilities=[
        Ability(
            title="Bench Guard",
            game_text="As long as Brock's Rhydon is Benched, whenever 1 of your Benched Pok\u00e9mon is damaged, you may do 10 of that damage to Brock's Rhydon instead. (If more than 1 of your Benched Pok\u00e9mon is damaged at the same time, you may use this power once for each of them.)",
            ability_type=AbilityTypes.POKE_POWER,
            passive=bench_guard_passive,
        ),
        Attack(
            title="Lariat",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=flip_or_nothing(),
        ),
    ],
)
