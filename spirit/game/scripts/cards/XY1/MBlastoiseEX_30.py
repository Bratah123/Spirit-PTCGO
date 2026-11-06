from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="01134ed3-152d-5b6f-a117-d32677995ef2",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBlastoiseEX.Name",
    display_name="M Blastoise-EX",
    searchable_by=["M Blastoise-EX", "MEGA", "EX", "MBlastoiseEX"],
    subtypes=["MEGA", "EX"],
    collector_number=30,
    set_code="XY1",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    family_id=9,
    abilities=[
        Attack(
            title="Hydro Bombard",
            game_text="This attack does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=snipe_attack(30, count=2, also_base=True),
        ),
    ],
)