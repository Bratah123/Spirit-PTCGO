from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import continuous_headbutt
from spirit.game.card_effects.sm6 import mountaintop_mining

card = PokemonCardDef(
    guid="d5b8d245-967d-5bda-b520-55bb2cbd135a",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name",
    display_name="Diggersby",
    searchable_by=["Diggersby", "Stage 1", "Diggersby"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    family_id=659,
    abilities=[
        Attack(
            title="Mountaintop Mining",
            game_text="You may do 40 more damage. If you do, discard the top 2 cards of your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=mountaintop_mining,
        ),
        Attack(
            title="Rock Cannon",
            game_text="Flip a coin until you get tails. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="x",
            effect=continuous_headbutt,
        ),
    ],
)
