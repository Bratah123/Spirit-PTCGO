from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack, self_energy_discard_attack
from spirit.game.card_effects.ecard import has_fire_energy_attached


card = PokemonCardDef(
    guid="d18c2539-2dc5-5824-9a1b-0bcded6a70a0",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Flamethrower",
            game_text="Discard 1 Fire Energy card attached to Arcanine in order to use this attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            condition=has_fire_energy_attached,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Take Down",
            game_text="Arcanine does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=recoil_attack(30),
        ),
    ],
)
