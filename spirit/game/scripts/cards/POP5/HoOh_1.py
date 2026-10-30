from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import fire_blast_discard


card = PokemonCardDef(
    guid="ab3b94f0-e89c-5123-a71d-03639fcf44f4",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy attached to Ho-Oh.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=fire_blast_discard(),
        ),
    ],
)
