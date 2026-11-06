from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="9f2cbc16-9a55-56fb-a385-08eb2345350a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    display_name="Monferno",
    searchable_by=["Monferno", "Stage 1", "Monferno"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Loud Howl",
            game_text="Your opponent Switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Fire Tail Slap",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)