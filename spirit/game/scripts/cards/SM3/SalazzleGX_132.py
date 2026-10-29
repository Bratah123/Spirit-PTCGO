from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import queens_haze_gx
from spirit.game.card_effects.attacks_common import count_prizes_taken, damage_per

card = PokemonCardDef(
    guid="3ac63e56-009b-55cf-a526-d478003c3ab0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalazzleGX.Name",
    display_name="Salazzle-GX",
    searchable_by=["Salazzle-GX", "Stage 1", "GX", "SalazzleGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=132,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=758,
    abilities=[
        Attack(
            title="Diabolical Claws",
            game_text="This attack does 50 damage for each Prize card you have taken.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_prizes_taken(), 50),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2},
            damage=110,
        ),
        Attack(
            title="Queen's Haze-GX",
            game_text="Discard all Energy from your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2},
            effect=queens_haze_gx,
        ),
    ],
)
